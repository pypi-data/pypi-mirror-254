; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [5 x i8] c"bool\00"
@1 = internal constant [5 x i8] c"meas\00"

define void @purelyclassical() local_unnamed_addr #0 {
entry:
  %0 = add i64 1, 2 ; 3
  %1 = add i64 %0, 3 ; 6
  %2 = sub i64 4, 2 ; 2
  %3 = add i64 %2, 1 ; 3
  %4 = add i64 %3, %1 ; 9
  %5 = sub i64 %1, %3 ; 3
  %6 = icmp ne i64 %1, %4
  br i1 %6, label %then, label %else
then:
  %7 = icmp ne i64 %2, %4 
  br i1 %7, label %nested_then, label %nested_else
nested_then:
  %8 = add i64 %5, 1; 4
  br label %fallthrough
nested_else:
  %9 = add i64 %5, 2; 5
  br label %fallthrough
else:
  %10 = add i64 %5, 3; 6
  br label %fallthrough
fallthrough:
  %11 = phi i64 [ %8, %nested_then ], [ %9, %nested_else ], [ %10, %else ]	
  %12 = icmp eq i64 %3, %2  
  %13 = select i1 %12, i1 0, i1 1
  call void @__quantum__rt__bool_record_output(i1 %13, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @0, i32 0, i32 0))
  br i1 %12, label %second_then, label %second_else
second_then:
  %14 = add i64 %4, 1; 10
  br label %exit
second_else:
  %15 = add i64 %4, 2; 11
  br label %exit
exit:
  %16 = phi i64 [ %14, %second_then ], [ %15, %second_else ]
  tail call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)  
  %17 = add i64 1, 2 ; 3
  %18 = sub i64 %17, 1 ; 5
  %19 = udiv i64 %17, 2 ; 2
  %20 = mul i64 %17, 2 ; 8
  %21 = shl i64 %17, 2 ; 4
  %22 = lshr i64 %17, 2 ; 1
  %23 = xor i64 %17, 2 ; 6
  %24 = and i64 %17, 2 ; 0
  %25 = or i64 17, 2 ; 10
  call void @__quantum__rt__result_record_output(%Result* null, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @1, i32 0, i32 0))    
  call void @__quantum__rt__int_record_output(i64 %11)
  call void @__quantum__rt__int_record_output(i64 %16)
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

declare void @__quantum__rt__bool_record_output(i1, i8*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__rt__result_record_output(%Result*, i8*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

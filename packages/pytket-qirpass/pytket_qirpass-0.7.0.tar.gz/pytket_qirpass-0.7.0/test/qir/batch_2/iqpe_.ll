; ModuleID = 'iqpe.bc'
source_filename = "LLVMDialectModule"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"cr0\00"

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__rz__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__rt__result_record_output(%Result*, i8*) local_unnamed_addr

declare void @__quantum__rt__array_end_record_output() local_unnamed_addr

declare void @__quantum__rt__array_start_record_output() local_unnamed_addr

declare i1 @__quantum__qis__read_result__body(%Result*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

define void @__nvqpp__mlirgen__iqpe() local_unnamed_addr #0 {
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %1 = tail call i1 @__quantum__qis__read_result__body(%Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  br i1 %1, label %2, label %3

2:                                                ; preds = %0
  tail call void @__quantum__qis__rz__body(double 0xBFF921FB54442D18, %Qubit* null)
  br label %3

3:                                                ; preds = %2, %0
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %4 = tail call i1 @__quantum__qis__read_result__body(%Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  br i1 %1, label %5, label %6

5:                                                ; preds = %3
  tail call void @__quantum__qis__rz__body(double 0xBFE921FB54442D18, %Qubit* null)
  br label %6

6:                                                ; preds = %5, %3
  br i1 %4, label %7, label %8

7:                                                ; preds = %6
  tail call void @__quantum__qis__rz__body(double 0xBFF921FB54442D18, %Qubit* null)
  br label %8

8:                                                ; preds = %7, %6
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %9 = tail call i1 @__quantum__qis__read_result__body(%Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__rz__body(double 0xBFEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__rz__body(double 0x3FEF6A7A2955385E, %Qubit* null)
  br i1 %1, label %10, label %11

10:                                               ; preds = %8
  tail call void @__quantum__qis__rz__body(double 0xBFD921FB54442D18, %Qubit* null)
  br label %11

11:                                               ; preds = %10, %8
  br i1 %4, label %12, label %13

12:                                               ; preds = %11
  tail call void @__quantum__qis__rz__body(double 0xBFE921FB54442D18, %Qubit* null)
  br label %13

13:                                               ; preds = %12, %11
  br i1 %9, label %14, label %15

14:                                               ; preds = %13
  tail call void @__quantum__qis__rz__body(double 0xBFF921FB54442D18, %Qubit* null)
  br label %15

15:                                               ; preds = %14, %13
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  tail call void @__quantum__rt__array_start_record_output()
  tail call void @__quantum__rt__result_record_output(%Result* null, i8* nonnull getelementptr inbounds ([4 x i8], [4 x i8]* @0, i64 0, i64 0))
  tail call void @__quantum__rt__array_end_record_output()
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="1" }

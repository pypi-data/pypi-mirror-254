source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__Interop() local_unnamed_addr #0 {
entry:
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x4012D97C7F3321D2, %Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %0, label %cont_1, label %else_1

cont_1:                                           ; preds = %entry
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x4012D97C7F3321D2, %Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* null)
  %1 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %1, label %then0__2.i.i.i, label %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit.1

else_1:                                           ; preds = %entry
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x401F6A7A2955385E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x4012D97C7F3321D2, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x3FF921FB54442D18, %Qubit* null)
  %2 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %2, label %then0__2.i.i.i, label %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit.1

then0__2.i.i.i:                                   ; preds = %else_1, %cont_1
  call void @__quantum__qis__reset__body(%Qubit* null)
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0x4025FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x3FEE91F42805715F, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x3FEE91F42805715F, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x3FEE91F42805715F, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rx__body(double 0x3FEE91F42805715F, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 8 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 9 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 10 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 11 to %Result*))
  call void @__quantum__qis__rx__body(double 0x3FEE91F42805715F, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0x4021475CC9EEDF00, %Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit.1

Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit.1: ; preds = %then0__2.i.i.i, %else_1, %cont_1
  call void @__quantum__qis__rz__body(double 0x4022D97C7F3321D2, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x400921FB54442D18, %Qubit* null)
  br label %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit

Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit: ; preds = %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit.1
  call void @__quantum__qis__rz__body(double 0x4022D97C7F3321D2, %Qubit* null)
  call void @__quantum__qis__rx__body(double 0x400921FB54442D18, %Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 12 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  ret void
}

declare i1 @__quantum__qis__anynonzero__body(%Result*, %Result*, %Result*, %Result*) local_unnamed_addr

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__rx__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__rz__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__rzz__body(double, %Qubit*, %Qubit*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="5" "requiredResults"="13" }
